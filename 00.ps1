param (
    [string]$filename,
    [string]$inputname,
    [string]$outputname,
    [int]$runs = 1,
    [string[]]$pyargs  # Accepts multiple arguments as an array
)

# Check if filename is provided
if (-not $filename) {
    Write-Host "Usage: .\00.ps1 <filename> [-inputname <inputname>] [-outputname <outputname>] [runs] [pyargs...]"
    exit 1
}

# Set default values for inputname and outputname if not provided
if (-not $inputname) {
    $inputname = "$filename.in"
}

if (-not $outputname) {
    $outputname = "$filename.out"
}

# Prepare the command
$pyargsStr = $pyargs -join ' '  # Join the array of Python arguments into a space-separated string
$command = "Get-Content '$inputname' | python '$filename.py' $pyargsStr > '$outputname'"

Write-Output "Running command: $command"

# Run the command for the specified number of times
for ($i = 0; $i -lt $runs; $i++) {
    Invoke-Expression $command
}
