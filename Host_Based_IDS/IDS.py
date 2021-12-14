import os
import sys
import hashlib
from datetime import datetime

SEPARATOR = " | "


def hash_bytes(bytes_iter, hasher):
	for block in bytes_iter:
		hasher.update(block)
	return hasher.hexdigest()


def file_as_block_iter(file, block_size=65536):
	block = file.read(block_size)
	while len(block) > 0:
		yield block
		block = file.read(block_size)
	file.close()


def hash_file(file_path):
	return hash_bytes(file_as_block_iter(open(file_path, 'rb')), hashlib.sha256())


def generate(path) -> {str: str}:  # returns dictionary of relative file path and hash
	"""generates a log file for the folder and it´s contents"""
	if os.path.exists(path):
		if os.path.isdir(path):
			# generate hash for all files in directory
			things = os.listdir(path)
			if len(things) > 0:
				result = {}
				for thing in things:
					result.update(generate(path+"/"+thing))
				return result
			return
		elif os.path.isfile(path):
			# generate hash for this file
			return {path: hash_file(path)}
	else:
		print(f"{path} is not a valid path")
		return


def save_generated_to_file(stuff: {str: str}):
	today = datetime.today()
	filename = today.strftime("%Y_%m_%d_%H_%M_%S_%f.idslog")
	try:
		file = open(filename, "w+")
		for key, value in stuff.items():
			file.write(f"{value}{SEPARATOR}{key}\n")
		file.close()
	except OSError:
		print("Failed to save file")
		return None
	return filename


def read_generated_file_to_dict(file_path):
	result = {}
	file = open(file_path, "r")
	line = file.readline()
	while len(line) > 0:  # if line is empty, end of file is reached
		line = line.strip().split(SEPARATOR)
		if line[1] in result:
			print(f"{file_path} is invalid, {line[1]} occurred more than once")
			return None
		if len(line) != 2:
			print(f"{file_path} is invalid, {line} is invalid entry")
			return None
		if len(line[0]) != 64:
			print(f"{file_path} is invalid, {line[0]} is not a sha256 hash")
			return None
		result[line[1]] = line[0]
		line = file.readline()
	file.close()
	return result


def compare(old, new, verbose=True):
	"""compares two log dictionaries and prints it´s differences"""
	if old == new:
		print("Logs are identical")
	else:
		print("[-] Missing, [+] New, [~] Changed, [=] Unchanged\n")
		done = []
		for key, value in old.items():
			if key not in new:
				print(f"[-] {key}")
			else:
				if old[key] == new[key]:
					if verbose:
						print(f"[=] {key}")
				else:
					print(f"[~] {key}")
			done.append(key)
		for key, value in new.items():
			if key not in done:
				if key not in old:
					print(f"[+] {key}")


def main():
	args = sys.argv[1:]
	if len(args) < 1:
		print("Missing arguments")
	else:

		if args[0] == "generate":
			result = generate(args[1])
			if len(result) > 0:
				saved_to = save_generated_to_file(result)
				if saved_to is not None:
					print(f"saved result to {saved_to}")
				else:
					return
			else:
				print("Path is empty or invalid!")
				return

		elif args[0] == "compare":
			if len(args[1:]) == 1:  # generate new log and compare it to the specified log
				old_dict = read_generated_file_to_dict(args[1])
				common_path = os.path.commonpath(list(old_dict.keys()))
				new_dict = generate(common_path)
				compare(old_dict, new_dict)
			elif len(args[1:]) == 2:
				old_dict = read_generated_file_to_dict(args[1])
				if old_dict is None:
					return
				new_dict = read_generated_file_to_dict(args[2])
				if new_dict is None:
					return
				compare(old_dict, new_dict)

		elif args[0] == "help":
			print("To generate a new log file use command:\ngenerate [path to file/folder]")
			print("To compare a log file with the current state use command:\ncompare [path to .idslog file]")
			print("To compare two log files use command:\ncompare [path to old .idslog file] [path to new .idslog file]")

		else:
			if os.path.exists(args[0]):
				# find and read newest idslog file
				paths = [(path, os.path.getctime(path)) for path in os.listdir(os.getcwd()) if path.endswith(".idslog")]
				newest_path = max(paths, key=lambda x: paths[1])[0]
				old_dict = read_generated_file_to_dict(newest_path)

				new_dict = generate(args[0])
				saved_to = save_generated_to_file(new_dict)
				if saved_to is not None:
					print(f"saved result to {saved_to}")
				else:
					return
	
				if old_dict is not None:
					compare(old_dict, new_dict)
			else:
				print("invalid path")


main()
