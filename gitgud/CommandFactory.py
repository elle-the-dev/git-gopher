from gitgud.CommandRunner import CommandRunner
from gitgud.Options import Options
from gitgud.VersionIncrementer import VersionIncrementer

from gitgud.Menu import Menu
from gitgud.CommandInterface import CommandInterface
from gitgud.Fzf import Fzf
from gitgud.GitDataGetter import GitDataGetter
from gitgud.CheckoutBranch import CheckoutBranch
from gitgud.CheckoutBranchRemote import CheckoutBranchRemote
from gitgud.CheckoutTag import CheckoutTag
from gitgud.BranchBranch import BranchBranch
from gitgud.BranchTag import BranchTag
from gitgud.MergeBranch import MergeBranch
from gitgud.MergeTag import MergeTag
from gitgud.MergeSquash import MergeSquash
from gitgud.Add import Add
from gitgud.Fetch import Fetch
from gitgud.TrackRemote import TrackRemote
from gitgud.UpstreamPush import UpstreamPush
from gitgud.PushTag import PushTag
from gitgud.TagIncrementVersion import TagIncrementVersion
from gitgud.DeleteBranch import DeleteBranch
from gitgud.DeleteBranchForce import DeleteBranchForce
from gitgud.DeleteTag import DeleteTag
from gitgud.DeleteTagRemote import DeleteTagRemote
from gitgud.Reset import Reset
from gitgud.ResetHard import ResetHard
from gitgud.CherryPick import CherryPick
from gitgud.DiffCommits import DiffCommits
from gitgud.DifftoolCommits import DifftoolCommits
from gitgud.DifftoolCommitsDirDiff import DifftoolCommitsDirDiff
from gitgud.History import History
from gitgud.HistoryDir import HistoryDir
from gitgud.StashMessage import StashMessage
from gitgud.StashPop import StashPop
from gitgud.StashApply import StashApply
from gitgud.StashDrop import StashDrop

class CommandFactory:
    def __init__(self):
        self._fzf = Fzf()
        self._git_data_getter = GitDataGetter(self._fzf)
        self._command_runner = CommandRunner(self._git_data_getter)

    def menu(self):
        options = Options()
        return Menu(self._command_runner, self._fzf, options)

    def checkout_branch(self):
        return CheckoutBranch(self._command_runner, self._git_data_getter)

    def checkout_branch_remote(self):
        return CheckoutBranchRemote(self._command_runner, self._git_data_getter)

    def checkout_tag(self):
        return CheckoutTag(self._command_runner, self._git_data_getter)

    def branch_branch(self):
        return BranchBranch(self._command_runner, self._git_data_getter)

    def branch_tag(self):
        return BranchTag(self._command_runner, self._git_data_getter)

    def merge_branch(self):
        return MergeBranch(self._command_runner, self._git_data_getter)

    def merge_tag(self):
        return MergeTag(self._command_runner, self._git_data_getter)

    def merge_squash(self):
        return MergeSquash(self._command_runner, self._git_data_getter)

    def fetch(self):
        return Fetch(self._command_runner, self._git_data_getter)

    def track_remote(self):
        return TrackRemote(self._command_runner, self._git_data_getter)

    def upstream_push(self):
        return UpstreamPush(self._command_runner, self._git_data_getter)

    def push_tag(self):
        return PushTag(self._command_runner, self._git_data_getter)

    def tag_increment_version(self):
        return TagIncrementVersion(self._command_runner, self._git_data_getter, VersionIncrementer())

    def delete_branch(self):
        return DeleteBranch(self._command_runner, self._git_data_getter)

    def delete_branch_force(self):
        return DeleteBranchForce(self._command_runner, self._git_data_getter)

    def delete_tag(self):
        return DeleteTag(self._command_runner, self._git_data_getter)

    def delete_tag_remote(self):
        return DeleteTagRemote(self._command_runner, self._git_data_getter)

    def reset(self):
        return Reset(self._command_runner, self._git_data_getter)

    def reset_hard(self):
        return ResetHard(self._command_runner, self._git_data_getter)

    def diff_commits(self):
        return DiffCommits(self._command_runner, self._git_data_getter)

    def difftool_commits(self):
        return DifftoolCommits(self._command_runner, self._git_data_getter)

    def difftool_commits_dir_diff(self):
        return DifftoolCommitsDirDiff(self._command_runner, self._git_data_getter)

    def history(self):
        return History(self._command_runner, self._git_data_getter)

    def history_dir(self):
        return HistoryDir(self._command_runner, self._git_data_getter)

    def stash_message(self):
        return StashMessage(self._command_runner, self._git_data_getter)

    def stash_pop(self):
        return StashPop(self._command_runner, self._git_data_getter)

    def stash_apply(self):
        return StashApply(self._command_runner, self._git_data_getter)

    def stash_drop(self):
        return StashDrop(self._command_runner, self._git_data_getter)

    def cherry_pick(self):
        return CherryPick(self._command_runner, self._git_data_getter)

    def add(self):
        return Add(self._command_runner, self._git_data_getter, self._fzf)

    def make(self, cmd) -> CommandInterface:
        switcher = {
            'menu': self.menu,
            'checkout-branch': self.checkout_branch,
            'checkout-branch-remote': self.checkout_branch_remote,
            'checkout-tag': self.checkout_tag,
            'branch-branch': self.branch_branch,
            'branch-tag': self.branch_tag,
            'merge-branch': self.merge_branch,
            'merge-tag': self.merge_tag,
            'merge-squash': self.merge_squash,
            'add': self.add,
            'fetch': self.fetch,
            'track-remote': self.track_remote,
            'upstream-push': self.upstream_push,
            'push-tag': self.push_tag,
            'tag-increment-version': self.tag_increment_version,
            'delete-branch': self.delete_branch,
            'delete-branch-force': self.delete_branch_force,
            'delete-tag': self.delete_tag,
            'delete-tag-remote': self.delete_tag_remote,
            'reset': self.reset,
            'reset-hard': self.reset_hard,
            'cherry-pick': self.cherry_pick,
            'diff-commits': self.diff_commits,
            'difftool-commits': self.difftool_commits,
            'difftool-commits-dir-diff': self.difftool_commits_dir_diff,
            'history': self.history,
            'history-dir': self.history_dir,
            'stash-message': self.stash_message,
            'stash-pop': self.stash_pop,
            'stash-apply': self.stash_apply,
        }

        func = switcher.get(cmd, lambda: "Error: Unknown command")
        return func()
