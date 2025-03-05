import java.io.*;
//import org.jetbrains.annotations.NotNull;

public static void runPython(String pythonFileName) {
    try {
        String pythonFilePath = "./" + pythonFileName;

        ProcessBuilder processBuilder = new ProcessBuilder("python3", "-u", pythonFilePath);
        Process process = processBuilder.start();

        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
        Thread outputThread = getThread(process, reader);

        Thread errorThread = new Thread(() -> {
            try {
                String line;
                while ((line = errorReader.readLine()) != null) {
                    System.err.println(line); // Print Python's errors
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        outputThread.start();
        errorThread.start();

        int exitCode = process.waitFor();
        println("Process finished with exit code " + exitCode);
    } catch (IOException | InterruptedException e) {
        e.printStackTrace();
    }
}

//@NotNull
private static Thread getThread(/*@NotNull*/ Process process, BufferedReader reader) {
    BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(process.getOutputStream()));

    return new Thread(() -> {
        try {
            String line;
            while ((line = reader.readLine()) != null) {
                println(line); // Print Python's output to Java's console
                BufferedReader userInputReader = new BufferedReader(new InputStreamReader(System.in));
                String userInput = userInputReader.readLine(); // Read user's input
                writer.write(userInput + "\n"); // Send input to Python
                writer.flush(); // Ensure it's sent immediately
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    });
}

void main() {
    runPython("test.py");
    System.exit(0);
}