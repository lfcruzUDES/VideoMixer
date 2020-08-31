from os import path
    
DIR_OF_THIS_SCRIPT = path.abspath( path.dirname( __file__ ) )
DIR_OF_THIRD_PARTY = path.join( DIR_OF_THIS_SCRIPT, 'env/lib/python3.8/site-packages/' )

def Settings( **kwargs ):
    return {
        'sys_path': [
            path.join(DIR_OF_THIRD_PARTY, 'pyyaml'),
            path.join(DIR_OF_THIRD_PARTY, 'ffmpeg'),
            path.join(DIR_OF_THIRD_PARTY, 'click'),
        ],
        'interpreter_path': './env/bin/python3.8'
    }
