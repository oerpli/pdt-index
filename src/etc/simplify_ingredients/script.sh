ls ../*csv | % {xsv select 2 $_ | sort | Get-Unique > ($_.Name)}
echo 'manually fix encoding errors resulting from powershell being wacky'