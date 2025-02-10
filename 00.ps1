param (
    [string]$filename
)

if (-not $filename) {
    Write-Host "Usage: .\script.ps1 <filename>"
    exit 1
}

Get-Content "$filename.in" | python "$filename.py" > "$filename.out"
