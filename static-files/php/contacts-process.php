<?php
if(!session_id()) {
	session_start();
}
error_reporting(0);

if (isset($_REQUEST['action'])) {
    if ($_REQUEST['action'] == "email_server_responce") {
        $ourMail = "info@cocukcacim.org"; //Insert your email address here
        $pre_messagebody_info = "";
        $errors = array();
        $data = array();
        parse_str($_REQUEST['values'], $data);
        
        $result = array(
            "is_errors" => 0,
            "info" => ""
        );
		
		if (!empty($errors)) {
            $result['is_errors'] = 1;
            $result['info'] = $errors;
            echo json_encode($result);
            exit;
        }

        $headers = 'MIME-Version: 1.0' . "\r\n";
        $headers.= 'Content-type: text/html; charset=UTF-8' . "\r\n";
        $headers.= "From: ".$data['email']."\r\n";
		$pre_messagebody_info.="<strong>Name</strong>" . ": " . $data['name'] . "<br />";
        if (! empty($data['email']) ) {
            $pre_messagebody_info.="<strong>E-mail</strong>" . ": " . $data['email'] . "<br />";
        }

       	$subject = "Website Contact Form";

        $after_message = "\r\n<br />--------------------------------------------------------------------------------------------------\r\n<br /> This mail was sent via contact form";

        if (mail($ourMail, $subject, $pre_messagebody_info .= $category . "<strong>Message</strong>" . ": " . $data['message'] .$after_message, $headers)) {
            $result["info"] = "success";
        } else {
            $result["info"] = "server_fail";
        }
        echo json_encode($result);
        exit;
    }
} ?>

