import subprocess
import os

class CmdBase:
    def __init__(self, wd):
        self.wd = wd

    def check_output(self, cmd):
        return subprocess.check_output(
            cmd, shell=True, cwd=self.wd).decode('utf-8', errors='replace')

    def call(self, cmd, cwd=None):
        return subprocess.call(cmd, shell=True, cwd=cwd or self.wd)

class CmdInvoice(CmdBase):

    def __init__(self, wd):
        CmdBase.__init__(self, wd)
        home_dir = os.path.expanduser('~')
        self.output_dir =  os.path.join(home_dir, 'Google\ Drive', 'invoices')
        self.output_dir2 =  os.path.join(home_dir, 'Google Drive', 'invoices')

    def pandoc(self, input_file):
        out_file_name = 'tmp/tmp.html'
        self.call('pandoc -s -S -o {} -H template/style.css {}'.format(
            out_file_name, input_file))
        return out_file_name

    def wkhtmltopdf(self, input_file, output_file_name):
        self.call('wkhtmltopdf -L 2cm -R 2.5cm -T 3cm {} {}'.format(
            input_file, os.path.join(self.output_dir, output_file_name)))

    def commit(self, output_file_name):
        self.call('git add .', cwd=self.output_dir2)
        self.call('git commit -m "{}"'.format(output_file_name), cwd=self.output_dir2)
        self.call('git push', cwd=self.output_dir2)

