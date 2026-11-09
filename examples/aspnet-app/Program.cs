using GardusiGustavo.Package;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => $"answer={Answer.Value}");

app.Run();
