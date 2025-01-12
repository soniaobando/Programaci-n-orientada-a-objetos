using
System;
using
System.Collections.Generic;
using
System.Linq;


class Program
    {
        static
    void
    Main(string[]
    args)
    {
    // Crear
    una
    lista
    para
    almacenar
    los
    números
    List < int > numerosGanadores = new
    List < int > ();

    // Definir
    constantes
    para
    la
    cantidad
    de
    números
    y
    rangos
    const
    int
    TOTAL_NUMEROS = 6;
    const
    int
    NUMERO_MINIMO = 1;
    const
    int
    NUMERO_MAXIMO = 49;

    // Pedir
    los
    números
    al
    usuario
    Console.WriteLine("Introduce los 6 números ganadores de la Lotería Primitiva:");

    for (int i = 0; i < TOTAL_NUMEROS; i++)
    {
        bool numeroValido = false;


while (!numeroValido)
    {
        Console.Write($"Introduce el número {i + 1}: ");
    if (int.TryParse(Console.ReadLine(), out int numero))
    {
    if (numero >= NUMERO_MINIMO & & numero <= NUMERO_MAXIMO)
    {
    if (!numerosGanadores.Contains(numero))
    {
    numerosGanadores.Add(numero);
    numeroValido = true;
    }
    else
    {
    Console.WriteLine("Este número ya ha sido introducido. Por favor, introduce otro número.");
    }
    }
    else
    {
    Console.WriteLine($"El número debe estar entre {NUMERO_MINIMO} y {NUMERO_MAXIMO}");
    }
    }
    else
    {
    Console.WriteLine("Por favor, introduce un número válido");
    }
    }
}

// Ordenar
los
números
de
menor
a
mayor
numerosGanadores.Sort();

// Mostrar
los
números
ordenados
Console.WriteLine("\nLos números ganadores ordenados de menor a mayor son:");
foreach(int
numero in numerosGanadores)
{
Console.Write($"{numero} ");
}

// Esperar
a
que
el
usuario
presione
una
tecla
antes
de
cerrar
Console.WriteLine("\n\nPresiona cualquier tecla para salir...");
Console.ReadKey();
}
}