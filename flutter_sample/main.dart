import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  Future<Uint8List?> fetchImage() async {
    try {
      final response = await http.get(Uri.parse('http://192.168.xx.x:5000/plot')); //give your ipv4 add here
      if (response.statusCode == 200) {
        return response.bodyBytes;
      } else {
        print('Failed to load image: ${response.statusCode}');
      }
    } catch (e) {
      print('Error fetching image: $e');
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Water Consumption Graph')),
        body: FutureBuilder<Uint8List?>(
          future: fetchImage(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const Center(child: CircularProgressIndicator());
            } else if (snapshot.hasData) {
              return Center(child: Image.memory(snapshot.data!));
            } else {
              return const Center(child: Text('❌ Couldn\'t load the graph. Make sure the Flask app is running.'));
            }
          },
        ),
      ),
    );
  }
}
