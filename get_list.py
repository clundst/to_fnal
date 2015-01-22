def get_list(config_path):
    import configparser
    cfg = configparser.ConfigParser()
    list = []
    cfg.read(config_path)
    path = cfg['FROM_T3']['path_to_files']
    print ("Path from config is = ", path, "\n")
    list = [1,23, 34 ]
    return(list)