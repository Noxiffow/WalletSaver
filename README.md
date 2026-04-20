# 💰 WalletSaver

**Salva tu cartera antes de que sea tarde**

Aplicación móvil Android de gestión financiera personal desarrollada como Trabajo Final de Grado (TFG) del Ciclo Formativo de Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM).

---

## 🎯 Descripción

WalletSaver es una aplicación de gestión financiera personal que prioriza la **privacidad**, **gratuidad** y **funcionamiento offline**. A diferencia de otras apps del mercado, no vende datos de usuarios, no tiene publicidad y funciona completamente sin conexión a Internet.

### ✨ Características principales

- 📊 **Dashboard interactivo** con gráficos de gastos por categoría
- 💸 **Registro de transacciones** con categorización y etiquetas
- 🎯 **Sistema de presupuestos** con alertas automáticas
- 🔒 **Privacidad total** - tus datos nunca se venden
- 📴 **Funcionamiento offline** - no necesitas Internet
- ☁️ **Sincronización opcional** multi-dispositivo
- 📈 **Gamificación** con rachas de ahorro

---

## 🛠️ Stack Tecnológico

### Backend
- **Framework:** FastAPI (Python)
- **Base de datos:** PostgreSQL (Supabase)
- **Autenticación:** JWT
- **Hosting:** Render/Railway

### Android App
- **Lenguaje:** Kotlin
- **UI Framework:** Jetpack Compose
- **Base de datos local:** Room (SQLite)
- **Networking:** Retrofit
- **Gráficos:** MPAndroidChart
- **Sincronización:** WorkManager

---

## 📋 Estado del Proyecto

🟡 **En desarrollo** - Fase 1: Diseño y Arquitectura

### Roadmap

- [x] Entrega 1: Propuesta de proyecto
- [ ] Fase 1: Diseño de arquitectura y modelo de datos (Semanas 1-2)
- [ ] Fase 2: Desarrollo del Backend (Semanas 3-5)
- [ ] Fase 3: Desarrollo de Android App (Semanas 6-10)
- [ ] Fase 4: Testing y Refinamiento (Semanas 11-12)
- [ ] Fase 5: Documentación y Defensa (Semanas 13-14)

---

## 🚀 Instalación

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Android App

1. Abre `android-app/` en Android Studio
2. Sincroniza dependencias de Gradle
3. Ejecuta en emulador o dispositivo físico

---

## 📚 Documentación

La documentación completa del proyecto se encuentra en la carpeta `docs/`:

- [Memoria TFG](docs/memoria_tfg.pdf)
- [Modelo de datos](docs/modelo_datos.md)
- [API Endpoints](docs/api_endpoints.md)
- [Guía de contribución](docs/CONTRIBUTING.md)

---

## 👨‍💻 Autor

**Jonathan Neto**  
Estudiante de 2º DAM - Curso 2024-2025

---

## 📄 Licencia

Este proyecto es código abierto bajo licencia MIT.
