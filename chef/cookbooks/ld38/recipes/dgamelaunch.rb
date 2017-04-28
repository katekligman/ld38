package "autoconf"
package "build-essential"
package "bison"
package "libncurses-dev"
package "flex"
package "libsqlite3-dev"
package "sqlite3"

git "/usr/local/dgamelaunch" do
  repository "https://github.com/paxed/dgamelaunch.git"
  reference "master"
  action :sync
end

execute "Install dgamelaunch" do
  cwd "/usr/local/dgamelaunch"
  command "./autogen.sh --enable-sqlite --enable-shmem && make"
end

template '/usr/local/dgamelaunch/dgl-create-chroot' do
  source 'dgl-create-chroot.erb'
  owner 'ld38'
  group 'ld38'
  mode '0776'
  variables({
    :chroot => '/home/ld38/game/',
    :usrgrp => 'ld38:ld38'
  })
end

execute "Create chroot for dgamelaunch" do
  cwd "/usr/local/dgamelaunch"
  command "./dgl-create-chroot"
  not_if { ::File.exist? '/home/ld38/game/'}
end
