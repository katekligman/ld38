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

group 'ld38'

user 'ld38' do
  group 'ld38'
  system true
  shell '/bin/bash'
end

