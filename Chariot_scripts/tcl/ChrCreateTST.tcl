
set e1 "localhost"
set e2 "localhost"
set script   "c:/Program Files (x86)/Ixia/IxChariot/Scripts/Throughput.scr"
set testFile "lbtest.tst"
set timeout 120
set TEST_DURATION  600

load ChariotExt
package require ChariotExt

# (2)
# You must create a test object to define a new test
# or to load an existing test from disk.
puts "Create the test..."
set test [chrTest new]
# set runopts [chrRunOpts new]

# (6.1)
# Create 10 pairs
for {set i 1} {$i <= 2} {incr i} {
    puts "$i pair"
    # Create a new pair
    set pair [chrPair new]                  
    # Set pair attributes
    chrPair set $pair E1_ADDR $e1 E2_ADDR $e2
    # Use the script for the pair
    chrPair useScript $pair $script
    chrPair setScriptVar $pair send_data_rate "1000 Mb"
    chrPair setScriptVar $pair file_size 299999999
    chrTest addPair $test $pair
}
# chrRunOpts set runopts TEST_DURATION 6000
set runOpts [chrTest getRunOpts $test]
# TEST_DURATION 1 to 359999
chrRunOpts set $runOpts TEST_DURATION $TEST_DURATION
chrRunOpts set $runOpts TEST_END FIXED_DURATION
# REPORTING_TYPE : BATCH, REALTIME 
chrRunOpts set $runOpts REPORTING_TYPE BATCH
puts "=========="
puts "Save the test..."
chrTest save $test $testFile
