# package-cs

C# reference package: a .NET library, an ASP.NET example, tests, and NuGet
release notes.

## Layout

| Path | Holds |
| --- | --- |
| `src/` | publishable library |
| `tests/` | xUnit tests |
| `examples/aspnet-app/` | full ASP.NET demo |
| `docs/` | usage and release notes |

## Build

```bash
dotnet test tests/GardusiGustavo.Package.Tests/GardusiGustavo.Package.Tests.csproj
```
