# Calorie Calculator (Calculadora de Calorías)

This small Python script calculates the daily calorie requirement based on the **Harris‑Benedict** equation. It works for both males (H) and females (M) and runs entirely in the console.

## How it works
1. The script prompts for your gender, age, height (cm) and weight (kg).
2. It selects the appropriate Harris‑Benedict formula:
   - **Male**: `66.47 + (13.75 * weight) + (5 * height) - (6.74 * age)`
   - **Female**: `655.1 + (9.56 * weight) + (1.85 * height) - (4.68 * age)`
3. It prints the estimated calories per day, the execution time, and the memory usage of the `calculadora` function.

## Usage
```bash
python "Calculadora de Calorias.py"
```
You will be prompted:
```
Cual es tu genero? (H/M) H
Cual es tu edad: 20
Cual es tu estatura en cm: 172
Cual es tu peso en kg: 84
```
The script will then output something like:
```
Base a tus datos, deberias de consumir 1946.67 calorias al dia
El tiempo que toma a la funcion ejecutarse fue de 18.20 segundos
La cantidad de memoria utilizada fue de 160.00 bytes
```

## Requirements
- Python 3.x (standard library only – no external dependencies).

## License
This script is released into the public domain (zero‑restriction). Feel free to fork, modify, or use it in your own projects.
