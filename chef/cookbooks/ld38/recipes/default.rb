#
# Cookbook:: game
# Recipe:: default
#
# Copyright:: 2017, The Authors, All Rights Reserved.

# THIS IS JUST TEST CODE
apt_update 'Update the apt cache daily' do
  frequency 86_400
  action :periodic
end
