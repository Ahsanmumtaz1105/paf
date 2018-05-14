import os
cur_dir = os.getcwd()
excluded_files_dirs = ['.idea', '.git', 'venv', '__pycache__', '__init__.py',
                       '.pyc']


def get_folder(fol_path):
    folders = []
    for _dir in os.listdir(fol_path):
        if _dir in excluded_files_dirs:
            continue
        if os.path.isdir(os.path.join(fol_path, _dir)):
            folders.append(_dir)
    return folders


def get_only_py_files(file_path):
    folder_path = [_f for _f in os.listdir(file_path) if not os.path.isfile(_f)]
    only_py_files = []
    for _f in folder_path:
        if _f == '__init__.py':
            continue
        if '.py' in _f:
            only_py_files.append(_f.split('.py')[0])
    return only_py_files


def create_folder(fol_path=None):
    if not fol_path:
        fol_path = 'docs'
    if not os.path.exists(fol_path):
        os.makedirs(fol_path, exist_ok=True)
    return fol_path


for _fol in get_folder(cur_dir):
    doc_path = create_folder(r'docs\{}'.format(_fol))
    path = os.path.join(cur_dir, _fol)

    py_files = get_only_py_files(path)
    for i in py_files:
        temp_doc_path = os.path.join(doc_path, i)
        cmd = "python -m robot.libdoc -f html {}.{} {}.html"
        os.system(cmd.format(_fol, i, temp_doc_path))

    fol = get_folder(path)
    if fol:
        for sub_fol in fol:
            fol_doc_path = create_folder(r'docs\{}\{}'.format(_fol, sub_fol))
            sub_path = os.path.join(path, sub_fol)
            py_files = get_only_py_files(sub_path)
            for j in py_files:
                fol_temp_doc_path = os.path.join(fol_doc_path, j)
                cmd = "python -m robot.libdoc -f html {}.{}.{} {}.html"
                os.system(cmd.format(_fol, sub_fol, j, fol_temp_doc_path))

            fol2 = get_folder(sub_path)
            if fol2:
                for sub_fol2 in fol2:
                    fol_doc_path2 = create_folder(
                        r'docs\{}\{}\{}'.format(_fol, sub_fol, sub_fol2))
                    sub_path2 = os.path.join(sub_path, sub_fol2)
                    py_files2 = get_only_py_files(sub_path2)
                    for k in py_files2:
                        # pdb.set_trace()
                        fol_temp_doc_path2 = os.path.join(fol_doc_path2, k)
                        cmd = "python -m robot.libdoc -f html {}.{}.{}.{} " \
                              "{}.html"
                        os.system(
                            cmd.format(_fol, sub_fol, sub_fol2, k,
                                       fol_temp_doc_path2))

                    fol3 = get_folder(sub_path2)
                    if fol3:
                        for sub_fol3 in fol3:
                            fol_doc_path3 = create_folder(
                                r'docs\{}\{}\{}\{}'.format(_fol, sub_fol,
                                                           sub_fol2, sub_fol3))
                            sub_path3 = os.path.join(sub_path2, sub_fol3)
                            py_files3 = get_only_py_files(sub_path3)
                            for l in py_files3:
                                # pdb.set_trace()
                                fol_temp_doc_path3 = os.path.join(fol_doc_path3,
                                                                  l)
                                cmd = "python -m robot.libdoc -f html " \
                                      "{}.{}.{}.{}.{} {}.html"
                                os.system(cmd.format(_fol, sub_fol, sub_fol2,
                                                     sub_fol3, l,
                                                     fol_temp_doc_path3))
