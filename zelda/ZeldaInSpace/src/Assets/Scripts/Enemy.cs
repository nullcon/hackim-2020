using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

using System;

public enum EnemyState
{
    walk,
    attack,
    idle,
    stagger
}



public class Enemy : MonoBehaviour {

    public float health;
    public string enemyName;
    public int baseAttack;
    public EnemyState currentState;
    public float moveSpeed;
    public GameObject textbox;
    public GUIStyle style;



    public FloatValue maxHealth;
    // Use this for initialization
    private void Awake()
    {
        health = maxHealth.initialValue;
        currentState = EnemyState.idle;
    }

    private void TakeDamage(float damage)
    {
        health -= damage;
        if (health <= 0)
        {
            StartCoroutine(ShowSome());

            this.gameObject.SetActive(false);
        }

    }
    public void Knock(Rigidbody2D myRigidbody, float knockTime, float damage)
    {
        StartCoroutine(KnockCo(myRigidbody, knockTime));
        TakeDamage(damage);
    }
    private void Start () {
        style.normal.textColor = Color.black;

    }
    private IEnumerator KnockCo(Rigidbody2D myRigidbody, float knockTime)
    {
        if (myRigidbody != null)
        {
            yield return new WaitForSeconds(knockTime);
            myRigidbody.velocity = Vector2.zero;
            currentState = EnemyState.idle;
            myRigidbody.velocity = Vector2.zero;
        }
    }
    private IEnumerator ShowSome()
    {
        textbox.SetActive(true);
        yield return new WaitForSeconds(3f);
        textbox.SetActive(false);
        yield return null;
    }
    // Update is called once per frame
    void Update () {
		
	}

    void OnGUI()
    {
        if (String.Equals(transform.name, "npc1"))
        {
            GUI.Label(new Rect(0, 0, 100, 100), health.ToString(), style);
        } else if  (string.Equals(transform.name, "npc2")) {
            GUI.Label(new Rect(102, 0, 202, 100), health.ToString(), style);
        } else if  (string.Equals(transform.name, "npc3")) {
            GUI.Label(new Rect(204, 0, 304, 100), health.ToString(), style);
        } else if  (string.Equals(transform.name, "npc4")) {
            GUI.Label(new Rect(306, 0, 406, 100), health.ToString(), style);
        } else if (string.Equals(transform.name, "npc5"))
        {
            GUI.Label(new Rect(408, 0, 508, 100), health.ToString(), style);
        }
    }
}
