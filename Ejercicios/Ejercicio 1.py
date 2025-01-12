using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // Crear una lista de asignaturas
        List<string> asignaturas = new List<string>
        {
            "Matemáticas",
            "Física",
            "Química",
            "Historia",
            "Lengua"
        };

        // Mostrar el título
        Console.WriteLine("Lista de Asignaturas del Curso:");
        Console.WriteLine("-------------------------------");

        // Mostrar cada asignatura con su número
        for (int i = 0; i < asignaturas.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {asignaturas[i]}");
        }

        // Esperar a que el usuario presione una tecla para cerrar
        Console.WriteLine("\nPresione cualquier tecla para salir...");
        Console.ReadKey();
    }
}