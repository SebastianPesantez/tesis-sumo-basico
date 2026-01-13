# Instalación de SUMO desde código fuente (Ubuntu 24.04 sobre WSL2)

Este documento describe **paso a paso** el proceso de instalación y compilación de **SUMO (Simulation of Urban MObility)** desde código fuente, utilizando **Ubuntu 24.04 LTS sobre WSL2**, incluyendo los problemas encontrados y sus soluciones.

> Este procedimiento fue validado durante el desarrollo del trabajo de titulación y se documenta para facilitar la reproducibilidad y evitar errores comunes.

---

## 1. Entorno de trabajo

* Sistema anfitrión: Windows 10/11
* Subsistema: WSL2
* Distribución: Ubuntu 24.04.3 LTS
* Kernel: 6.6.x-microsoft-standard-WSL2
* CPU: 16 núcleos
* RAM asignada: ~8 GB
* Python: 3.12

SUMO se compiló directamente desde el repositorio oficial:

* [https://github.com/eclipse-sumo/sumo](https://github.com/eclipse-sumo/sumo)

---

## 2. Verificación inicial de WSL2

En PowerShell:

```powershell
wsl --list --verbose
```

Se debe verificar que Ubuntu esté en **VERSION 2**.

Dentro de Ubuntu:

```bash
uname -r
```

Debe aparecer `WSL2` en la salida.

---

## 3. Soporte gráfico en WSL2

Para habilitar y verificar aplicaciones gráficas:

```bash
sudo apt update
sudo apt install x11-apps -y
xclock
```

Si la ventana del reloj se abre correctamente, el entorno gráfico está listo para `sumo-gui` y `netedit`.

---

## 4. Instalación de dependencias del sistema

### Dependencias base

```bash
sudo apt install -y \
 git cmake g++ python3 python3-dev \
 libxerces-c-dev libfox-1.6-dev \
 libproj-dev libgdal-dev \
 libgl2ps-dev swig \
 default-jdk maven \
 libeigen3-dev
```

### Dependencias adicionales

```bash
sudo apt install -y \
 ccache libavformat-dev libswscale-dev \
 libopenscenegraph-dev \
 libgtest-dev gettext \
 xvfb tkdiff \
 python3-full python3-venv \
 python3-pip python3-setuptools
```

---

## 5. Clonado del repositorio de SUMO

```bash
cd ~
git clone --recursive https://github.com/eclipse-sumo/sumo
```

---

## 6. Variables de entorno

### SUMO_HOME

```bash
export SUMO_HOME=$HOME/sumo
```

Agregar permanentemente en `~/.bashrc`:

```bash
export SUMO_HOME=$HOME/sumo
```

### PYTHONPATH (necesario para TraCI)

```bash
export PYTHONPATH=$SUMO_HOME/tools
```

También debe añadirse al `~/.bashrc`.

---

## 7. Entorno virtual de Python (PEP 668)

Ubuntu 24.04 implementa la política **PEP 668**, que impide instalar paquetes con `pip` en el Python del sistema.

### Creación del entorno virtual

```bash
cd ~
python3 -m venv sumo-venv
source ~/sumo-venv/bin/activate
```

### Instalación de dependencias Python

```bash
cd ~/sumo
pip install --upgrade pip
pip install -r tools/requirements.txt
```

### Verificación de TraCI

```bash
python -c "import traci; print('TraCI OK')"
```

---

## 8. Configuración y compilación de SUMO

### Configuración con CMake

```bash
cd ~/sumo
cmake -B build .
```

Durante esta etapa pueden aparecer *warnings* relacionados con Arrow, Parquet, JuPedSim o Boost. Estos no son críticos y no afectan el funcionamiento principal de SUMO.

### Compilación

```bash
cmake --build build -j$(nproc)
```

---

## 9. Verificación de la instalación

```bash
~/sumo/bin/sumo --version
~/sumo/bin/sumo-gui
~/sumo/bin/netedit
```

Si las aplicaciones se ejecutan correctamente, la instalación es exitosa.

---

## 10. Notas finales

* SUMO **no se incluye** en el repositorio GitHub del proyecto.
* El entorno virtual `sumo-venv` tampoco se versiona.
* Este procedimiento permite reproducir el entorno completo sin necesidad de máquinas virtuales.

---

**Autor:** Sebastián Pesántez
**Contexto:** Trabajo de titulación – Simulación y control de tráfico vehicular con SUMO
