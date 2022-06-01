conda info
conda info --env
conda --version
conda update anaconda

conda create --name snowflakes numpy
conda create --name snakes python=3.9
conda create --name snakes python=3.9 "numpy>1" pandas

conda activate snowflakes
conda activate /path/to/environment-dir
conda activate
conda deactivate

conda search numpy
conda install numpy
conda list
conda list --name ENVNAME

conda create --clone ENVNAME --name NEWENV
conda list --explicit > pkgs.txt
conda create --name NEWENV --file pkgs.txt
conda env export --name ENVNAME > envname.yml
conda env create --file envname.yml

conda install conda-forge::numpy
conda install numpy==3.1.5
conda install "numpy[version='3.1.2|3.1.4']"
conda install "numpy>2,5,<3.2"
conda config --add channels CHANNELNAME

conda clean -all
conda uninstall numpy --name NEWNAME
conda update numpy --name NEWNAME
conda update --all --name NEWNAME