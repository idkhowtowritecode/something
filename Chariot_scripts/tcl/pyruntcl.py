import subprocess

# Path to your Tcl script
tcl_script_path = 'ChrCreateTST.tcl'

# Execute the Tcl script
result = subprocess.run(['tclsh', tcl_script_path], capture_output=True, text=True)

# Print the output and error (if any)
print('Output:', result.stdout)
print('Error:', result.stderr)
