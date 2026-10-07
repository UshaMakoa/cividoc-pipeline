param(
    [string]$Site = "generated-user-en",
    [string]$Page = "",
    [switch]$Build,
    [switch]$Strict,
    [switch]$Unit
)

$arguments = @("quick_test.py", "--site", $Site)
if ($Page) { $arguments += @("--page", $Page) }
if ($Build) { $arguments += "--build" }
if ($Strict) { $arguments += "--strict" }
if ($Unit) { $arguments += "--unit" }

& python @arguments
exit $LASTEXITCODE
