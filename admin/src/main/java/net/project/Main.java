package net.project;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

/**
 * @author learnercys
 * Created on 3/4/15.
 */
public class Main extends Application {

    public static final String APP_TITLE = "Controller Administrator";
    public void start ( Stage primary ) throws IOException{
        BorderPane root = FXMLLoader.load( getClass().getResource("fxml/mainctrl.fxml"));
        primary.setTitle( APP_TITLE );
        primary.setScene( new Scene( root ) );
        primary.show();
    }

    public static void main ( String[] args ) {
        launch( args );
    }
}
