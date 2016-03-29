# API Banco - Cliente .NET

Firmado de documentos XML, PDF utilizando un cliente .NET/C# y el API de firma electrónica.

### Requisitos
- .NET Framework 4.6.1
- Visual Studio 2015 Update 1 -- Opcional

### Configuración

Verificar la configuración de HttpClient con respecto a la propiedad BaseAddress en la línea 92 del archivo Program.cs. La configuración debe ser la siguiente:

```C#
client.BaseAddress = new Uri("http://proxy-banco.modernizacion.gob.cl/v1/files/");
client.DefaultRequestHeaders.Accept.Clear();
client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
```
