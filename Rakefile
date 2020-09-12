# development task, action on git repo
#
# this on host
#
require 'rake/clean'

pv_ver = '0.0.4'
RPMS = Rake::FileList.new ("#{Dir.home}/rpmbuild/RPMS/**")

puts "to be cleaned #{RPMS}, #{Dir.home}"
CLEAN.include  [ "#{RPMS}" ]

task 'addpvplot' do
  `git subtree add --prefix pvplot  git@github.com:timcoote/pvplot.git master --squash`
end

# these on guest
# setup rpmbuild environment
file "#{Dir.home}/rpmbuild/" do
  `rpmdev-setuptree`
end

# Documentation of shiny-server installation. Not needed on host or guest, only monitoring computer
task 'install-shiny-server' do
    `curl -O https://download3.rstudio.org/centos6.3/x86_64/shiny-server-1.5.14.948-x86_64.rpm`
    `sudo dnf install -y --nogpgcheck shiny-server-1.5.14.948-x86_64.rpm`
end

pv_mon_tar = "pv-monitoring.#{pv_ver}.tar.gz"
sources = FileList.new ("#{Dir.home}/rpmbuild/SOURCES/aurora.patch")

task 'rpm' => FileList["#{Dir.home}/rpmbuild/", pv_mon_tar, 'get_sources'] do |t|
  puts t.prerequisites
  `rpmbuild -ba packaging/pv-monitoring.spec`
  # switch causes unvalidated download of source
  `rpmbuild --undefine=_disable_source_fetch -ba packaging/aurora.spec`
end


file pv_mon_tar => FileList['shiny-server.conf', 'aurora/*', 'pvplot/today/*'] do |f|
  # need to check that this is on guest?
  #`tar czvf pv-monitor.0.0.1.tar.gz pvplot/today/* shiny-server.conf`
  puts "sources: #{f.prerequisites.all?}"
  `tar czvf pv-monitoring.#{pv_ver}.tar.gz pvplot/today/*  aurora/ shiny-server.conf --transform='s,^,pv-monitoring-#{pv_ver}/,'`
  #`tar czvf pv-monitoring.0.0.1.tar.gz --transform='s,^,pv-monitoring-0.0.1/,' pvplot/today/*  aurora/ shiny-server.conf`
end

task 'get_sources' do
  `cp pv-monitoring.#{pv_ver}.tar.gz packaging/aurora.patch ~/rpmbuild/SOURCES`
end

task 'forward' do
  # put rpms on to target box.
  `scp ~/rpmbuild/RPMS/*/* #{ENV["monitoring"]}:`
end

task 'buildchroot' do
  `sudo dnf install -y qemu-system-aarch64 qemu-user-static virt-manager`
end

task 'mkchroot' do
  `sudo dnf install --releasever=32 --installroot=/tmp/F32ARM --forcearch=aarch64 --repo=fedora --repo=updates systemd passwd dnf fedora-release vim-minimal cmake  python3 gcc-c++ tar gcc git make rubygem-rake iputils rpmdevtools -y`
end


file 'iid' => FileList['Rakefile'] do
  `buildah bud --override-arch arm64 --iidfile iid .`
end
