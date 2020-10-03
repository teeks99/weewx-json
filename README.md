# weewx-json
Extension for JSON output from weewx

This extension provides a skin that is not designed to be used from a web browser, rather for consumption from another
type of client...smartphone app, dynamic javascript page, automated bot.

This is most of the same data that can be found in the default "Seasons" report's `rss.xml` output, but formatted in
the JSON format for easier consumption by clients.


## Installing

Download the latest release from the [github releases](https://github.com/teeks99/weewx-json/releases) page

Run `wee_extension --install=weewx-json_X.X.tar.gz`

This will automatically add a `[[JSONReport]]` to your weewx.conf file that will include the `weewx.json` in your 
`HTML_ROOT`. 

## Uninstalling

Run `wee_extension --uninstall=weewx-json`