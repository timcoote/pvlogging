# development task, action on git repo
#
# this on host
#
require 'rake/clean'

pv_ver = '0.0.3'
RPMS = Rake::FileList.new ("#{Dir.home}/rpmbuild/RPMS/**")

puts "to be cleaned #{RPMS}, #{Dir.home}"
CLEAN.include  [ "#{RPMS}" ]

task 'addpvplot' do
  `git subtree add --prefix pvplot  git@github.com:timcoote/pvplot.git master --squash`
end

# these on guest
# setup rpmbuild environment
file '~/rpmbuild' do
  `rpmdev-setuptree`
end



# packaging tasks
#task 'packageup' do
#  `echo "tar up the source files into?? and put them where they\'re needed"`
#  `tar xzvf ~/rpmbuild/SOURCES/tarball.tar.gz shiny-server.conf`
#end

pv_mon_tar = "pv-monitoring.#{pv_ver}.tar.gz"

task 'rpm' => FileList[pv_mon_tar] do
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
  `cp pv-monitoring.#{pv_ver}.tar.gz packaging/aurora.patch ~/rpmbuild/SOURCES`
end

task 'forward' do
  # put rpms on to target box.
  `scp ~/rpmbuild/RPMS/*/* #{ENV["monitoring"]}:`
end
