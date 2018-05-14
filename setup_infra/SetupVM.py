"""
To setup the pre-req, and methods which are required as part of initialization.
"""
import os
import traceback
from shutil import copyfile
from setup_infra import VMData
import subprocess


class SetupVM:
    """
        Class Name -  SetupVM
        Description - This class is contains properties properties and methods to be used for Create new VM,
        Installl download and install Control Suite/Equitrac build.
        Return - None
        Author -  Ahsan Mumtaz
        Modification date - 28-Apr-2018
        """

    files_to_copy = VMData.files_to_copy
    powershell_path = "powershell.exe"
    powershell_script_path = VMData.psFile_path
    powershell_file_temp_dir = r"C:\\Temp\\"
    cred_file_path = VMData.cred_file_path
    folder_name_IVT = VMData.folder_IVT
    folder_name_server_columbus = VMData.folder_columbus
    folder_name_server_vasco = VMData.folder_vasco
    VM_name_prefix = VMData.vm_name_prefix
    VMHost = VMData.vmHost
    destinationFiles = r"C:\\temp\\"
    logs_path = r"C:\temp\VM_Setup.log"
    domain_name = VMData.domain_name
    domain_admin_user = VMData.domain_admin_name
    domain_admin_pwd = VMData.domain_admin_pwd
    domain_userId = VMData.domain_user
    domain_user_pwd = VMData.domain_pwd
    VM_user_name = VMData.VM_user_name
    VM_user_pwd = VMData.VM_user_pwd
    is_control_suite = "TRUE"
    is_eq = "TRUE"
    cs_base_path = VMData.cs_installer_base_path
    control_suite = VMData.cs_core_comp_version
    eq_base_path = VMData.eq_base_path
    os_cus_spec = VMData.os_cus_spec
    wat_branch = VMData.main_base_path
    cs_absolute_path = None
    folder_name = None
    datastore = None
    template = None
    wat_absolute_branch = None
    eq_absolute_path = None

    @staticmethod
    def set_data_store(team):
        """
        Function Name -  set_data_store
        Description - Set the VMSphere datastore based on the value of the value of data from VmData File
        Parameters - team i.e. IVT, columbus or vasco
        Return - None
        Author -  Ahsan Mumtaz
        Modification date - 26-Apr-2018
        """
        try:
            if team == 'ivt':
                SetupVM.datastore = VMData.datastore_ivt
                SetupVM.folder_name = SetupVM.folder_name_IVT
            elif team == 'columbus':
                SetupVM.datastore = VMData.datastore_server
                SetupVM.folder_name = SetupVM.folder_name_server_columbus
            elif team == 'vasco':
                SetupVM.datastore = VMData.datastore_server
                SetupVM.folder_name = SetupVM.folder_name_server_vasco
            else:
                raise ValueError('Invalid Team: ' + team)
        except Exception as e:
            print(traceback.format_exc())

    @staticmethod
    def set_template(platform):
        """
        Function Name -  set_template
        Description - Set the template name to deploy the new VM, it will take the platform and based on the set the
        template from which the vm would be deployed
        Parameters:
            platform: platform name(i.e. win2k16)
        Return - None
        Author - Ahsan Mumtaz
        Modification date - 28-Apr-2018
        """
        try:
            if platform == 'win2k16':
                SetupVM.template = VMData.template_win2k16

            elif platform == 'win2k12r2':
                SetupVM.template = VMData.template_win2k12r2

            else:
                raise ValueError('Invalid platform:' + platform)

        except:
            'Invalid platform:' + platform

    @staticmethod
    def copy_files_from_ntwrk_directory(source_path: object, target_path: object,
                                        files: object) -> object:
        """
        Function Name -  copy_files_from_ntwrk_directory
        Description - To Copy the build files from network shared directory
        Parameters:
            source_path: directory path from where builds files would be copied.
            target_path: directory path to which build would be copied.
        Author - Ahsan Mumtaz
        Modification date - 28-Apr-2018
        :type files: object
        """
        try:
            for file in files:
                source_file_path = source_path + r"\\" + file
                target_file_path = target_path + r"\\" + file
                copyfile(source_file_path, target_file_path)
        except Exception as e:
            print(traceback.format_exc())

    @staticmethod
    def get_eq_build():
        """
        Function Name:  get_eq_build
        Description: This is to get the files from build repository to network shared directory.
        Parameters: None
        Return: None
        Author: Ahsan Mumtaz
        Modification date: 28-Apr-2018
        """
        try:
            is_exist = os.path.isdir(SetupVM.eq_absolute_path)
            file_not_exist = []
            if is_exist:
                lst_file_to_copy = SetupVM.files_to_copy.split(';')
                for file in lst_file_to_copy:
                    filepath = SetupVM.eq_absolute_path + r"\\" + file
                    if not os.path.exists(filepath):
                        file_not_exist.append(file)
                        SetupVM.copy_files_from_ntwrk_directory(
                            SetupVM.wat_absolute_branch,
                            SetupVM.eq_absolute_path, file_not_exist)
            else:
                os.mkdir(SetupVM.eq_absolute_path)
                SetupVM.copy_files_from_ntwrk_directory(
                    SetupVM.wat_absolute_branch, SetupVM.eq_absolute_path,
                    file_not_exist)
        except Exception as e:
            print(traceback.format_exc())

    @staticmethod
    def deploy_vm_and_install(vm_name, is_control_suite, is_equitrac, eq_build_version):
        """
        Function Name:  deploy_vm_and_install
        Description: This is to deploy the vm and install the Control Suite and Equitrac.
        Parameters:
            vm_name: Equitrac Server vm
            is_control_suite: (bool) True to install Control suite
            is_equitrac: (bool) True to install Equitrac
            eq_build_version: Equitrac build version to be deployed
        Return: None
        Author: Ahsan Mumtaz
        Modification date: 28-Apr-2018
        """
        eq_build_path = None
        eq_build_path = SetupVM.eq_absolute_path + r"\*.*"

        p = subprocess.Popen(
            [SetupVM.powershell_path, SetupVM.powershell_script_path,
             SetupVM.cred_file_path, SetupVM.folder_name, vm_name,
             SetupVM.VMHost, SetupVM.datastore, SetupVM.template,
             SetupVM.logs_path, SetupVM.domain_name, SetupVM.domain_admin_user,
             SetupVM.domain_admin_pwd, SetupVM.VM_user_name,
             SetupVM.VM_user_pwd, SetupVM.domain_userId,
             SetupVM.domain_user_pwd, str(is_control_suite),
             str(is_equitrac), eq_build_version, SetupVM.cs_absolute_path,
             eq_build_path, SetupVM.os_cus_spec],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        out, err = p.communicate()
        import sys, pdb
        pdb.Pdb(stdout=sys.__stdout__).set_trace()

    def install_equitrac6(self, eq_build_ver, vm_name, team='ivt', platform='win2k16', is_control_suite=True,
                          is_equitrac=True, branch='main'):
        """
        Function Name:  install_equitrac6
        Description: To install equitrac 6 build to the new VM
        Parameters:
            eq_build_ver: Equitrac build version to be installed.
            vm_name: new VM Name
            team: Team name
            platform: Equitrac windows platform
            is_control_suite: Install Control Suite
            is_equitrac: Install Equitrac
            branch: Branch from which build would be downloaded
        Return: None
        Author: Ahsan Mumtaz
        Modification date: 28-Apr-2018
        """
        if is_control_suite:
            SetupVM.cs_absolute_path = SetupVM.cs_base_path + '\\' + SetupVM.control_suite + r'\*.*'

        SetupVM.set_data_store(team)
        SetupVM.set_template(platform)
        SetupVM.eq_absolute_path = SetupVM.eq_base_path + eq_build_ver
        if branch == 'main':
            SetupVM.wat_absolute_branch = SetupVM.wat_branch + eq_build_ver
        else:
            SetupVM.wat_absolute_branch = branch + eq_build_ver

        # Copy Build from network directory
        SetupVM.get_eq_build()

        SetupVM.deploy_vm_and_install(vm_name, is_control_suite, is_equitrac,
                                      eq_build_ver)

