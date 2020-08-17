# development task, action on git repo
#
# this on host
task 'addpvplot' do
  `git subtree add --prefix pvplot  git@github.com:timcoote/pvplot.git master --squash`
end

# these on guest
# setup rpmbuild environment
file '~/rpmbuild' do
  `rpmdev-setuptree`
end



# packaging tasks
task 'packageup' do
  `echo "tar up the source files into?? and put them where they\'re needed"`
  `tar xzvf ~/rpmbuild/SOURCES/tarball.tar.gz shiny-server.conf`
end

task 'rpm' do
  `rpmbuild -ba pv-monitoring.spec`
end


task 'tarup' do
  #`tar czvf pv-monitor.0.0.1.tar.gz pvplot/today/* shiny-server.conf`
  `tar czvf pv-monitoring.0.0.1.tar.gz pvplot/today/* --transform='s,^,pv-monitoring-0.0.1/,' shiny-server.conf aurora`
end
