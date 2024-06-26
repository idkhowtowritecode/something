import subprocess

# Variables to pass to the Tcl script
e1 = '127.0.0.1'
e2 = 'localhost'
pairs = 5

# Path to your Tcl script
tcl_script_path = 'ChrCreateTST1.tcl'

# Execute the Tcl script with arguments
result = subprocess.run(['tclsh', tcl_script_path, e1, e2, str(pairs)], capture_output=True, text=True)

# Print the output and error (if any)
print('Output:', result.stdout)
print('Error:', result.stderr)
