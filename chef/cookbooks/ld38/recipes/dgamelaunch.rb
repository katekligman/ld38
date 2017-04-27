package "autoconf"
package "build-essential"
package "bison"
package "libncurses-dev"
package "flex"

git "/usr/local/dgamelaunch" do
  repository "https://github.com/paxed/dgamelaunch.git"
  reference "master"
  action :sync
end

execute "Install dgamelaunch" do
  cwd "/usr/local/dgamelaunch"
  command "./autogen.sh && make"
end
