# Retrieve command-line arguments
set e1 [lindex $argv 0]
set e2 [lindex $argv 1]
set pairs [lindex $argv 2]
set script   "c:/Program Files (x86)/Ixia/IxChariot/Scripts/Throughput.scr"
set testFile "lbtest.tst"
set timeout 120
set TEST_DURATION  600

load ChariotExt
package require ChariotExt

puts "Create the test..."
set test [chrTest new]

for {set i 1} {$i <= $pairs} {incr i} {
    puts "$i pair"
    set pair [chrPair new]
    chrPair set $pair E1_ADDR $e1 E2_ADDR $e2
    chrPair useScript $pair $script
    chrPair setScriptVar $pair send_data_rate "1000 Mb"
    chrPair setScriptVar $pair file_size 299999999
    chrTest addPair $test $pair
}

set runOpts [chrTest getRunOpts $test]
chrRunOpts set $runOpts TEST_DURATION $TEST_DURATION
chrRunOpts set $runOpts TEST_END FIXED_DURATION
chrRunOpts set $runOpts REPORTING_TYPE BATCH

puts "=========="
puts "Save the test..."
chrTest save $test $testFile
