import functools
import time
import os
import sys


def read_strings(fname):
  with open(fname, "r") as file:
    return [line.strip() for line in file.readlines()]


def read_ints(fname):
  return [int(line) for line in read_strings(fname)]


def read_floats(fname):
  return [float(line) for line in read_strings(fname)]


def _get_curr_file_folder():
  return os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.dirname(sys.argv[0]))


def with_input(func):
  @functools.wraps(func)
  def wrapper_decorator(*args, **kwargs):
      # Do something before
      path = _get_curr_file_folder()
      lines = read_strings(f"{path}/input")
      value = func(lines, *args, **kwargs)
      # Do something after
      return value
  return wrapper_decorator

def with_sample(func):
  @functools.wraps(func)
  def wrapper_decorator(*args, **kwargs):
      # Do something before
      path = _get_curr_file_folder()
      lines = read_strings(f"{path}/sample")
      value = func(lines, *args, **kwargs)
      # Do something after
      return value
  return wrapper_decorator


def with_strings(fname):
  def decorator_with_strings(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        lines = read_strings(fname)
        value = func(lines, *args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
  return decorator_with_strings

def with_ints(fname):
  def decorator_with_ints(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        lines = read_ints(fname)
        value = func(lines, *args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
  return decorator_with_ints


def with_cols(fname, cols):
  def decorator_with_cols(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
      lines_raw = read_strings(fname)
      print(lines_raw[:10])
      lines = []

      for l in lines_raw:
        ls = l.split(" ")
        lt = []

        for i, ll in enumerate(ls):
          if cols[i] == 'int':
            lt.append(int(ll))
          elif cols[i] == 'float':
            lt.append(float(ll))
          else:
            lt.append(ll)

        lines.append(lt)

      value = func(lines, *args, **kwargs)
      # Do something after
      return value
    return wrapper_decorator
  return decorator_with_cols



def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
