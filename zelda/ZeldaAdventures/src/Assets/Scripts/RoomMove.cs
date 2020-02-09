using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;


public class RoomMove : MonoBehaviour {

    public Vector2 cameraChange;
    public Vector3 playerChange;
    private CameraMovement cam;
    public bool needText;
    public string placeName;
    public GameObject text;
    public Text placeText;



    // Use this for initialization
    void Start () {
        cam = Camera.main.GetComponent<CameraMovement>();
    }

    // Update is called once per frame
    void Update () {
		
	}

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            Debug.Log(placeText.text);

            if (String.Equals(placeText.text, "Home") || String.Equals(placeText.text, "Home!"))
            {
                cam.minPosition.x = -30.5f;
                cam.minPosition.y = 7.6f;
                cam.maxPosition.x = -28f;
                cam.maxPosition.y = 9.6f;
            }
            else if (String.Equals(placeText.text, "HackerTown!"))
            {

                cam.minPosition.x = -5.5f;
                cam.minPosition.y = -2f;
                cam.maxPosition.x = 18f;
                cam.maxPosition.y = 19.5f;
            }
            else if (String.Equals(placeText.text, "Flagtown!"))
            {
                cam.minPosition.x = -0.5f;
                cam.minPosition.y = 19.5f;
                cam.maxPosition.x = 14f;
                cam.maxPosition.y = 89.5f;
            }
            else if (String.Equals(placeText.text, "The Jungle!"))
            {
                cam.minPosition.x = -151f;
                cam.minPosition.y = -87.9f;
                cam.maxPosition.x = 146f;
                cam.maxPosition.y = 167.4f;
            }
            else if (String.Equals(placeText.text, "The Secret Place!"))
            {
                cam.minPosition.x = 71.5f;
                cam.minPosition.y = -102f;
                cam.maxPosition.x = 120.6f;
                cam.maxPosition.y = -99.2f;

            }
            else {
                cam.minPosition += cameraChange;
                cam.maxPosition += cameraChange;
            }

            other.transform.position += playerChange;
            if (needText)
            {
                StartCoroutine(whereAtPlace());
            }

        }
    }

    private IEnumerator whereAtPlace()
    {
        text.SetActive(true);
        placeText.text = placeName;
        yield return new WaitForSeconds(3f);
        text.SetActive(false);
    }
}
