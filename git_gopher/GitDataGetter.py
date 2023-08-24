from os import path
from re import sub
import readline # fix backspace and arrow keys on input
from subprocess import check_output, CalledProcessError
from colorama import Fore
from git_gopher.FormatColumns import FormatColumns
from git_gopher.NoTagsException import NoTagsException

class GitDataGetter:
    def __init__(self, fzf, command_runner):
        self._fzf = fzf
        self._command_runner = command_runner

    def get_current_branch_name(self):
        return self._command_runner.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip().strip("'")

    def get_branch_name(self, options=[], preview="git config branch.{2}.description"):
        return self._get_branches(options, preview, '--no-multi')

    def get_branch_names(self, options=[], preview="git config branch.{2}.description"):
        return self._get_branches(options, preview, '--multi')

    def _get_branches(self, options, preview, multi):
        format_columns = FormatColumns()
        branches = self._command_runner.check_output(['git', '--no-pager', 'branch', *options, '--format=%(if)%(HEAD)%(then)%(else)%(if:equals=HEAD)%(refname:strip=3)%(then)%(else)branch | %(refname:short)%(end)%(end)']).decode()
        branches = self._command_runner.check_output(['sed', '/^$/d'], input=str.encode(format_columns.set_colors({0: Fore.BLUE}).format(branches)))
        lines = self._fzf.run(branches.decode(), preview=preview, multi=multi)

        if lines:
            if multi == '--multi':
                return list(map(lambda line: line.split('\t')[1].strip(), lines.splitlines()))
            else:
                return lines.split('\t')[1].strip()

    def get_branch_names_remote(self, remote, preview=""):
        format_columns = FormatColumns()
        branches = check_output(['git', 'ls-remote', '--heads', remote]).decode()
        branches = list(map(lambda line: 'branch|' + line.split()[1].strip().replace('refs/heads/', ''), branches.splitlines()))
        lines = self._fzf.run(format_columns.set_colors({0: Fore.BLUE}).format('\n'.join(branches)))
        return list(map(lambda line: line.split('\t')[1].strip(), lines.splitlines()))

    def get_tag_name_from_tags(self, tags, options=[], preview="", multi="--no-multi"):
        format_columns = FormatColumns()

        # prepend 'tag' to each line
        tags = self._prefix_lines_with(tags, 'tag').splitlines()
        tags.reverse()
        tags = '\n'.join(tags)

        if not tags:
            raise NoTagsException

        lines = self._fzf.run(format_columns.set_colors({ 0: Fore.BLUE }).format(tags), preview=preview, multi=multi)

        if lines:
            if multi == '--multi':
                return list(map(lambda line: line.split('\t')[1].strip(), lines.splitlines()))
            else:
                return lines.split('\t')[1].strip()

    def get_tag_name(self, options=[], preview=""):
        tags = self._command_runner.check_output(['git', '--no-pager', 'tag']).decode()
        return self.get_tag_name_from_tags(tags, options, preview)

    def get_tag_names(self, options=[], preview=""):
        tags = self._command_runner.check_output(['git', '--no-pager', 'tag']).decode()
        return self.get_tag_name_from_tags(tags, options, preview, '--multi')

    def get_tag_name_remote(self, remote, options=[], preview=""):
        tags = self.get_remote_tags(remote)
        return self.get_tag_name_from_tags('\n'.join(tags), options, preview)

    def get_tag_names_remote(self, remote, options=[], preview=""):
        tags = self.get_remote_tags(remote)
        return self.get_tag_name_from_tags('\n'.join(tags), options, preview, '--multi')

    def get_local_tag_name(self, remote, options = [], preview=""):
        format_columns = FormatColumns()
        local_tags = list(map(lambda line : line.split()[1].strip(), self._command_runner.check_output(['git', 'show-ref', '--tags']).decode().splitlines()))
        remote_tags = self.get_remote_tags(remote)
        unpushed_tags = set(local_tags) - set(remote_tags)
        unpushed_tags = '\n'.join(list(map(lambda tag : tag.split('/')[2], unpushed_tags)))
        line = self._fzf.run(format_columns.set_colors({ 0: Fore.BLUE }).format(self._prefix_lines_with(unpushed_tags, 'tag')), preview=preview)

        if line:
            return line.split('\t')[1].strip()

    def get_remote_name(self, preview=""):
        format_columns = FormatColumns()
        remotes_list = list(set(self._command_runner.check_output(['git', 'remote', '-v']).decode().splitlines()))
        remotes = ""

        for line in remotes_list:
            if "push" in line:
                line = sub(r'\s+\(push\)', '', line)
                line = self._replace_tab_with_pipe(line)
                line = "remote | " + line
                remotes += line + "\n"

        line = self._fzf.run(format_columns.set_colors({ 0: Fore.BLUE }).format(remotes), preview=preview)

        if line:
            return line.split('\t')[1].strip()

    def get_remote_tags(self, remote: str):
        return  list(map(lambda line : line.split()[1].strip(), self._command_runner.check_output(['git', 'ls-remote', '--tags', remote]).decode().splitlines()))

    def get_commit_hash(self, branch=None, preview=""):
        cmd = ['git', 'log', '--color=always']

        if branch:
            cmd.append(branch)

        cmd.append("--pretty=format:%C(blue)%h%C(reset)|%ad|%an|%C(yellow)%d %C(reset)%s")
        cmd.append('--date=relative')

        format_columns = FormatColumns()
        log_entries = self._command_runner.check_output(cmd).decode()
        line = self._fzf.run(format_columns.format(log_entries), preview=preview)
        return line.split('\t')[0].strip()

    def get_stash_ref(self, preview=""):
        format_columns = FormatColumns()
        DIR = path.dirname(path.realpath(__file__))
        preview = "echo {1} | xargs git stash show -p | cat <(echo -n \"" + preview + "\n\nALT+J: Down | ALT+K: Up\n----------------------------\n\n\") - | ggo-colorize"
        stashes = '\n'.join(list(map(lambda line: sub(':', ' |', line), self._command_runner.check_output(['git', 'stash', 'list']).decode().splitlines())))
        stash = self._fzf.run(format_columns.set_colors({0: Fore.BLUE}).format(stashes), preview=preview, preview_window="--preview-window=right")

        if stash:
            return stash.split('\t')[0]

    def get_git_dir(self):
        return self._command_runner.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip()

    def get_unstaged_files(self):
        return self._command_runner.check_output(['git', 'ls-files', self.get_git_dir(), '--exclude-standard', '--others', '-m']).decode()

    def get_unstaged_files_from_dir(self, git_dir):
        return self._command_runner.check_output(['git', 'ls-files', git_dir, '--exclude-standard', '--others', '-m']).decode()

    def get_is_tracked(self, file):
        return bool(self._command_runner.check_output(['git', 'ls-files', file]))

    def get_most_recent_tag(self):
        return self._command_runner.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()

    def get_semantic_part(self, preview=None):
        options = "Part|Patch\nPart|Minor\nPart|Major"
        format_columns = FormatColumns()
        selection = self._fzf.run(format_columns.set_colors({0: Fore.BLUE}).format(options), preview=preview)
        if selection:
            return selection.split('\t')[1].strip()

    def get_diff(self, file_path):
        return self._command_runner.check_output(['git', 'diff', file_path]).decode()

    def get_stash_contents(self, stash_ref):
        return self._command_runner.check_output(['git', 'stash', 'show', '-p', stash_ref]).decode()

    def remote_branch_exists(self, remote: str):
        try:
            return bool(self._command_runner.check_output(['git', 'show-ref', 'refs/remotes/' + remote]))
        except CalledProcessError:
            return False

    def local_branch_exists(self, local_branch):
        try:
            return bool(self._command_runner.check_output(['git', 'show-ref', 'refs/heads/' + local_branch]))
        except CalledProcessError:
            return False

    def checkout_branch_remote_command(self, branch: str):
        if not self.remote_branch_exists(branch):
            return ['git', 'checkout', branch]

        local_branch = sub(r'^.*\/', '', branch)
        if (not self.local_branch_exists(local_branch)):
            return ['git', 'checkout', '--track', branch]

        return ['git', 'checkout', local_branch]

    def get_branch_name_from_input(self):
        return input("New branch name: ")

    def get_stash_message_from_input(self, preview=''):
        print(preview)
        return input("Message: ")

    def _prefix_lines_with(self, lines, prefix: str):
        return sub(r'(?m)^(.)', prefix + r' | \1', lines)

    def _replace_tab_with_pipe(self, text: str):
        return sub(r'(?m)\t', ' | ', text)
