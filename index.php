<?php
// var_dump($_POST);
$command = escapeshellcmd('python app.py');
// var_dump($command);
if (isset($_POST['variable'])) {
    $input = $_POST['variable'];
    if (isset($_POST['variable'])) {

        $output = shell_exec("python app.py $input");
    }
}
// var_dump($input);

// var_dump($output);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">


    <link rel="stylesheet" href="styles/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Document</title>
</head>

<body>
    <form action="" method="post">
        <div class="img">
            <div class="parent">
                <div class="child">
                    <?php
                    if (isset($_POST['variable'])) {
                        $print = str_replace($input,  ' ', $output);
                        // str_replace();

                        // var_dump($output);
                        // var_dump($print);
                        echo "<h4> $print <h4> ";
                    }
                    ?>
                    <div class="enter-title"> What are your symptoms? </div>
                    <input type="text" name="variable" placeholder="Type your main symptom here" title="" autocomplete="off" class="text_box">
                </div>
                <input type="submit" class="btn btn-outline-danger but" href="#" role="button" value="Check"></input>
            </div>
        </div>
    </form>

</body>

</html>