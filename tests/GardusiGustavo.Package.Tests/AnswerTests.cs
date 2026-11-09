using Xunit;

namespace GardusiGustavo.Package.Tests;

public class AnswerTests
{
    [Fact]
    public void AnswerIs42() => Assert.Equal(42, Answer.Value);
}
