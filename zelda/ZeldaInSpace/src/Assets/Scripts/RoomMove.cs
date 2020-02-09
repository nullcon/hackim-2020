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
            PlayerAttrs pa = other.GetComponent<PlayerAttrs>();

            Debug.Log(placeText.text);

            if (string.Equals(placeText.text, "CheckPoint 1!"))
            {

                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "pepper"))
                {
                    pa.checkpoints.Add("pepper");
                }
                Debug.Log(pa.checkpoints.Count);
            }
            else if (string.Equals(placeText.text, "CheckPoint 2!"))
            {

                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "salt"))
                {
                    pa.checkpoints.Add("salt");
                }
                Debug.Log(pa.checkpoints.Count);
            }
            else if (string.Equals(placeText.text, "CheckPoint 3!"))
            {

                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "chilly"))
                {
                    pa.checkpoints.Add("chilly");
                }
                Debug.Log(pa.checkpoints.Count);
            }
            else if (string.Equals(placeText.text, "CheckPoint 4!"))
            {

                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "pickles"))
                {
                    pa.checkpoints.Add("pickles");
                }
                Debug.Log(pa.checkpoints.Count);
            }
            else if (string.Equals(placeText.text, "CheckPoint 5!"))
            {

                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "oregano"))
                {
                    pa.checkpoints.Add("oregano");
                }
                Debug.Log(pa.checkpoints.Count);
            }
            else if (string.Equals(placeText.text, "CheckPoint 6!"))
            {

                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "masala"))
                {
                    pa.checkpoints.Add("masala");
                }
                Debug.Log(pa.checkpoints.Count);
            }
            else if (string.Equals(placeText.text, "Final"))
            {
                Debug.Log("Hey welcome to final!\n");
                string last = pa.checkpoints[pa.checkpoints.Count - 1];
                if (!string.Equals(last, "final"))
                {
                    pa.checkpoints.Add("final");
                }
                Debug.Log(pa.checkpoints.Count);
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
