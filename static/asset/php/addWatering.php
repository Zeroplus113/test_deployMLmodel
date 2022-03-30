<?php
session_start();
include '../../connectDB.php';


    if(isset($_POST['Greenhouse'])) {
    $greenhouseID = $_POST['Greenhouse'];

    $sql = "SELECT MAX(periodID) AS currentPeriod FROM plant_period WHERE greenhouseID = '$greenhouseID' ";
    $result = $con->query($sql);
    $count_row = mysqli_num_rows($result);

    if($count_row !=0){
            while($rs = $result->fetch_assoc()){
                    $periodID = $rs['currentPeriod'];
                    // echo $periodID;
            }
        }


    $sql2 = "INSERT INTO watering(periodID,greenhouseID) VALUES('$periodID','$greenhouseID')";
    $con->query($sql2);






    $sql3 = "SELECT greenhouseID,periodID FROM watering WHERE greenhouseID = '$greenhouseID' AND periodID = '$periodID' ";
    $result2 = $con->query($sql3);
    $count_row2 = mysqli_num_rows($result2);


    if($count_row2!=0){
        while($rs2 = $result2->fetch_assoc()){
            $_SESSION['greenhouseID'] = $rs2['greenhouseID'];
            $_SESSION['periodID'] = $rs2['periodID'];
            header("location:../../dailycare/water.php");
            }
        }
    }

?>