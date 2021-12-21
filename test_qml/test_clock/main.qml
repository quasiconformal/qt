import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 500
    height: 300
    title: "Clock"
    property string currTime: "00:00:00"

    Rectangle {
        anchors.fill: parent

        Image {
            anchors.fill: parent
            source: "./images/background.png"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"

            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                //text: "16:38:33"
                text: currTime  // used to be; text: "16:38:33"
                font.pixelSize: 24
                color: "white"
            }

        }

    }

}