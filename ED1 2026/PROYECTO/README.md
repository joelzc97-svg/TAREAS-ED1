# 🎓 Sistema de Gestión de Estudiantes — INF220

Aplicación de escritorio para la gestión de estudiantes universitarios, desarrollada en Python con arquitectura **MVC (Modelo-Vista-Controlador)**. Permite inscribir, consultar, visualizar notas y dar de baja a estudiantes, con persistencia de datos en un archivo local JSON.

---

## 📁 Estructura del Proyecto

```
PROYECTO ED1/
├── main.py          # Punto de entrada de la aplicación
├── model.py         # Lógica de datos (lista enlazada + persistencia)
├── view.py          # Interfaz gráfica (CustomTkinter)
├── controller.py    # Intermediario entre modelo y vista
└── estudiantes.txt  # Archivo de persistencia (generado automáticamente)
```

---

## 🧱 Arquitectura MVC

### `model.py` — Modelo
Contiene la lógica de negocio y la estructura de datos.

- **`Estudiante`**: Clase nodo que representa a un estudiante con los atributos `id`, `nombre`, `apellido`, `calificaciones` y un puntero `siguiente` (estructura de lista enlazada simple).
- **`GestionEstudiantes`**: Clase principal de gestión. Implementa una **lista enlazada** para almacenar los estudiantes en memoria. Métodos principales:

| Método | Descripción |
|---|---|
| `inscribir(id, nombre, apellido, calificaciones)` | Agrega un estudiante al inicio de la lista |
| `dar_de_baja(id)` | Elimina un estudiante por su ID |
| `buscar(id)` | Retorna el nodo del estudiante si existe |
| `guardar_en_archivo()` | Serializa la lista a `estudiantes.txt` (JSON) |
| `cargar_desde_archivo()` | Carga los datos al iniciar la aplicación |

---

### `view.py` — Vista
Interfaz gráfica construida con **CustomTkinter** (tema oscuro, color `blue`). La ventana principal (1100×600 px) está dividida en dos paneles:

**Panel lateral (sidebar):**
- Campos de entrada: ID, Nombre, Apellido, Notas (separadas por coma)
- Botón **Inscribir** (verde)
- Botón **Ver Notas por ID** (azul)
- Botón **Dar de Baja** (rojo)

**Panel principal:**
- Tabla (`ttk.Treeview`) con las columnas: `ID`, `Nombre`, `Apellido`, `Promedio`, `Estado`
- Las filas se colorean automáticamente:
  - 🟢 **Verde** → Aprobado (promedio ≥ 51)
  - 🔴 **Rojo** → Reprobado (promedio < 51)

---

### `controller.py` — Controlador
Coordina la comunicación entre el modelo y la vista.

| Método | Descripción |
|---|---|
| `inscribir()` | Valida los campos y registra un nuevo estudiante |
| `eliminar()` | Solicita confirmación y da de baja al estudiante por ID |
| `ver_notas()` | Muestra las calificaciones individuales en un cuadro de diálogo |
| `actualizar_tabla()` | Refresca el `Treeview` con los datos actuales del modelo |

El controlador vincula los botones de la vista a sus respectivos métodos y sincroniza la tabla automáticamente tras cada operación.

---

### `main.py` — Punto de Entrada
Inicializa los tres componentes MVC y arranca el bucle principal de la interfaz.

```python
from model import GestionEstudiantes
from view import EstudianteView
from controller import EstudianteController

if __name__ == "__main__":
    modelo = GestionEstudiantes()
    vista = EstudianteView()
    app = EstudianteController(modelo, vista)
    vista.mainloop()
```

---

## ⚙️ Requisitos

- Python **3.10** o superior
- Librerías:

```bash
pip install customtkinter
```

> `tkinter` y `json` son parte de la biblioteca estándar de Python, no requieren instalación adicional.

---

## 🚀 Instalación y Ejecución

1. Clona o descomprime el proyecto:
   ```bash
   unzip PROYECTO_ED1.zip
   cd "PROYECTO ED1"
   ```

2. Instala las dependencias:
   ```bash
   pip install customtkinter
   ```

3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

---

## 💾 Persistencia de Datos

Los datos se almacenan automáticamente en `estudiantes.txt` en formato JSON cada vez que se realiza una operación de escritura. Ejemplo del formato:

```json
[
    {
        "id": "001",
        "nombre": "Ana",
        "apellido": "Pérez",
        "calificaciones": [75.0, 80.0, 60.0]
    }
]
```

El archivo se crea en el mismo directorio donde se ejecuta `main.py`. Si no existe al iniciar la aplicación, se crea vacío automáticamente.

---

## 📊 Lógica de Aprobación

El promedio se calcula como la media aritmética de todas las calificaciones ingresadas:

```
promedio = sum(calificaciones) / len(calificaciones)
```

| Promedio | Estado |
|---|---|
| ≥ 51 | ✅ APROBADO |
| < 51 | ❌ REPROBADO |

---

## 🗂️ Estructura de Datos Interna

Los estudiantes se almacenan en una **lista enlazada simple**. Cada nuevo estudiante se inserta al **inicio** de la lista (`O(1)`). La búsqueda y eliminación recorren la lista de forma secuencial (`O(n)`).

```
cabeza → [Est. C] → [Est. B] → [Est. A] → None
         (último    (segundo   (primero
         inscrito)  inscrito)  inscrito)
```

---

## 👤 Autor

**JOEL ZAMBRANA CORDOVA**

Proyecto desarrollado para la asignatura **INF220**.

---
