from subprocess import check_output, CalledProcessError

class Fzf:
    def run(self, options: str, preview: str="", preview_window: str="--preview-window=down:5", multi: str="--no-multi"):
        cmd: list = ['fzf', '--no-sort', '--no-hscroll', '--ansi', multi, '--preview='+preview, preview_window]
        try:
            return check_output(cmd, input=str.encode(options)).decode()
        except CalledProcessError as e:
            return
