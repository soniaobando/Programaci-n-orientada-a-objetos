public class Persona
{
    public string Nombre { get; set; }
    public int Id { get; set; }

    public Persona(string nombre, int id)
    {
        Nombre = nombre;
        Id = id;
    }
}
using System.Collections.Generic;

public class Cola
{
    private Queue<Persona> personas;

    public Cola()
    {
        personas = new Queue<Persona>();
    }

    // Añadir persona a la cola
    public void Encolar(Persona persona)
    {
        personas.Enqueue(persona);
    }

    // Verificar si la cola está vacía
    public bool EstaVacia()
    {
        return personas.Count == 0;
    }

    // Obtener la siguiente persona en la cola
    public Persona ObtenerSiguiente()
    {
        return personas.Peek();
    }

    // Eliminar la persona que acaba de subir
    public void Desencolar()
    {
        if (!EstaVacia())
        {
            personas.Dequeue();
        }
    }
}
using System.Collections.Generic;

public class Cola
{
    private Queue<Persona> personas;

    public Cola()
    {
        personas = new Queue<Persona>();
    }

    // Añadir persona a la cola
    public void Encolar(Persona persona)
    {
        personas.Enqueue(persona);
    }

    // Verificar si la cola está vacía
    public bool EstaVacia()
    {
        return personas.Count == 0;
    }

    // Obtener la siguiente persona en la cola
    public Persona ObtenerSiguiente()
    {
        return personas.Peek();
    }

    // Eliminar la persona que acaba de subir
    public void Desencolar()
    {
        if (!EstaVacia())
        {
            personas.Dequeue();
        }
    }
}
public class Atractivo
{
    private Cola cola;

    public Atractivo(Cola cola)
    {
        this.cola = cola;
    }

    public void SubirAlAtractivo()
    {
        if (!cola.EstaVacia())
        {
            Persona siguientePersona = cola.ObtenerSiguiente();
            Console.WriteLine($"{siguientePersona.Nombre} sube al atractivo.");
            cola.Desencolar();
        }
        else
        {
            Console.WriteLine("No hay más personas en la cola.");
        }
    }
}
using System;

class Program
{
    static void Main(string[] args)
    {
        Cola cola = new Cola();

        // Añadir personas a la cola
        cola.Encolar(new Persona("Carlos", 1));
        cola.Encolar(new Persona("Ana", 2));
        cola.Encolar(new Persona("Luis", 3));

        // Crear la instancia del atractivo
        Atractivo atractivo = new Atractivo(cola);

        // Simular que suben las personas en orden
        for (int i = 0; i < 3; i++)
        {
            atractivo.SubirAlAtractivo();
        }
    }
}
