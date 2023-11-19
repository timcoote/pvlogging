# PV logging on Fedora

## Introduction

This repo was an exercise in using rpm to package multiple services, specifically capturing and plotting solar panel performance. The plotting repo is separately
at `github.com/timcoote/pvplot`. It started out with the intention of running Shiny-Server over IPv6 with proprietary fixes for 32bit computers. Now it works with
a standard Shiny Server - although not packaged as a Fedora rpm - and includes some fixes to R that broke the original code (`https://bit.ly/30sfAeg`).

## Basic Workflow

- spin up vagrant box
- update versions in Rakefile and packaging/*spec (needs automating)
- on vagrant box, in directory `/vagrant`, `rake rpm`; `rake forward` (requires target username@name/address of monitoring/plotting computer in the env var `monitoring`).
- on linux box `sudo rpm -Uvh pv-monitoring<latestversion> aurora<latestversion>` (assumes already installed, services - `aurora-logging` and `shiny-server` are up and running. The rpm will restart the services, but not kick them off if not started.
- plots appear on `http://monitoring-and-plotting-computer/today/`

## Moving Parts
`Rakefile` captures most of the major activities. Not wholly broken down into dependencies, yet.
`aurora` various additional files to run the `aurora` query tool on a regular basis to capture output from the Aurora One PV inverter
`packaging` files to package up the `aurora` code and the framework that runs it and the `shiny-server` plotting code.
`pvplot` checkout of the shiny-server plotting code, with embedded knownledge of where the logged pv data are. This also includes other plotting experiments that are not used.

# TODO
- notification of systemd services - partially complete, but see here: https://bit.ly/2R4a0ZY. Non-trivial for remove/install cycle as default enabled packages are defined external to packages.
- build rpms for aarch64 using the resin.io tools.
- sort out firewall on target box, eg with `firewall-cmd --add-port=tcp/80
