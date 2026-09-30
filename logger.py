
import sys


class OutLogger(object):
    def __init__(self, logfile) -> None:
        self.term = sys.stdout
        self.log = open(logfile, "w", encoding='utf-8', buffering=1)
        self.filepath = logfile

    def __del__(self):
        self.close()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.close()

    def write(self, msg):
        self.term.write(msg)
        self.log.write(msg)

    def flush(self):
        if 'flush' in dir(self.term):
            self.term.flush()
        if 'flush' in dir(self.log):
            self.log.flush()
        if 'fileno' in dir(self.log):
            os.fsync(self.log.fileno())

    def close(self):
        if self.term is not None:
            sys.stdout = self.term
            self.term = None
        if self.log is not None:
            self.log.close()
            self.log = None


class ErrLogger(OutLogger):

    def __init__(self, logfile) -> None:
        self.term = sys.stderr
        self.log = open(logfile, "w", encoding='utf-8', buffering=1)
        self.filepath = logfile

    def close(self):
        if self.term is not None:
            sys.stderr = self.term
            self.term = None

        if self.log is not None:
            self.log.close()
            self.log = None
