# 🧮 Calculadora con Funciones en Python

Proyecto desarrollado en Python como parte de una serie de retos de programación enfocados en fortalecer los fundamentos del lenguaje y las buenas prácticas de desarrollo.

La aplicación permite realizar operaciones matemáticas básicas desde la consola mediante un menú interactivo y una estructura modular basada en funciones y archivos independientes.

---

# 📌 Descripción

Esta calculadora permite al usuario realizar las cuatro operaciones matemáticas básicas:

* Suma
* Resta
* Multiplicación
* División

El programa se ejecuta desde la consola y presenta un menú interactivo para seleccionar la operación deseada. Cada operación se encuentra implementada en un módulo independiente, promoviendo una mejor organización y mantenimiento del código.

---

# 🎯 Objetivos del Proyecto

* Practicar la creación y uso de funciones.
* Comprender la modularización de aplicaciones en Python.
* Utilizar la importación de módulos.
* Implementar menús interactivos en consola.
* Aplicar estructuras de control modernas como `match-case`.
* Gestionar errores simples como la división entre cero.

---

# 🚀 Características

✅ Menú interactivo en consola.

✅ Operaciones matemáticas básicas:

* Suma
* Resta
* Multiplicación
* División

✅ Arquitectura modular.

✅ Uso de funciones independientes para cada operación.

✅ Validación para evitar divisiones entre cero.

✅ Ejecución continua hasta que el usuario decida salir.

---

# 🛠️ Tecnologías Utilizadas

* Python 3
* Funciones
* Módulos
* Importación de archivos
* Bucles (`while`)
* Estructuras condicionales
* `match-case` (Python 3.10+)

---

# 📂 Estructura del Proyecto

```text
calculadora-con-funciones/
│
├── main.py
├── menu_interactivo.py
├── sumar.py
├── restar.py
├── multiplicar.py
├── division.py
└── README.md
```

### Descripción de archivos

| Archivo               | Función                                                          |
| --------------------- | ---------------------------------------------------------------- |
| `main.py`             | Punto de entrada del programa                                    |
| `menu_interactivo.py` | Controla el menú y la navegación                                 |
| `sumar.py`            | Realiza la operación de suma                                     |
| `restar.py`           | Realiza la operación de resta                                    |
| `multiplicar.py`      | Realiza la operación de multiplicación                           |
| `division.py`         | Realiza la operación de división y valida la división entre cero |

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/Anthony140823/Calculadora-usando-funciones-en-Python.git
```

## 2. Acceder al directorio

```bash
cd RETO-CALCULADORA CON FUNCIONES
```

## 3. Ejecutar el programa

```bash
python main.py
```

---

# ▶️ Uso

Al iniciar el programa se mostrará el siguiente menú:

```text
Operaciones que puedes realizar:

1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir
```

El usuario selecciona una opción e ingresa dos valores numéricos para obtener el resultado.

### Ejemplo

```text
Escoge una opción: 1

Dame el valor 1: 15
Dame el valor 2: 8

El resultado de la suma es: 23.00
```

---

# 🧠 Conceptos Aplicados

Durante el desarrollo de este proyecto se pusieron en práctica los siguientes conceptos:

* Definición y uso de funciones.
* Modularización de aplicaciones.
* Importación de módulos.
* Uso de parámetros y variables locales.
* Formateo de cadenas con f-strings.
* Estructuras repetitivas (`while`).
* Estructuras de selección (`match-case`).
* Manejo básico de errores lógicos.
* Organización de proyectos Python en múltiples archivos.

---

# 📈 Aprendizajes Obtenidos

Este proyecto permitió reforzar conocimientos fundamentales de Python como:

* Separar responsabilidades en distintos módulos.
* Mantener un código más limpio y escalable.
* Mejorar la reutilización de funciones.
* Comprender el flujo de ejecución entre archivos Python.
* Aplicar validaciones básicas para evitar errores de ejecución.

---

# 🔮 Mejoras Futuras

Algunas mejoras que podrían implementarse en futuras versiones:

* Validación de entradas no numéricas.
* Manejo de excepciones con `try-except`.
* Historial de operaciones realizadas.
* Operaciones avanzadas (potencias, raíces, porcentajes).
* Interfaz gráfica utilizando Tkinter.
* Pruebas unitarias con `unittest` o `pytest`.
* Empaquetar la aplicación como ejecutable.

---

# 👨‍💻 Autor

**Anthony JeanPaul Reyes Risco**

Desarrollador de software en formación apasionado por el aprendizaje continuo, la programación y la construcción de proyectos prácticos para fortalecer sus habilidades técnicas.

---

# 📄 Licencia

Este proyecto fue desarrollado con fines educativos y forma parte de mi portafolio personal de aprendizaje en Python.
