package com.example.practical3

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class Main : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btn = findViewById<Button>(R.id.buttonNavigate)

        btn.setOnClickListener {

            // Intent → Second Activity
            val intent = Intent(this, SecondActivity::class.java)
            startActivity(intent)

            // Start Service
            val serviceIntent = Intent(this, MyService::class.java)
            startService(serviceIntent)

            // Broadcast
            val broadcastIntent = Intent("com.example.practical3.MY_BROADCAST")
            sendBroadcast(broadcastIntent)
        }
    }
}
