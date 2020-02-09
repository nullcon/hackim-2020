using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public enum PlayerState
{
    walk,
    attack,
    stagger,
    idle
}

public class PlayerMovement : MonoBehaviour {


    public PlayerState currentState;

    public float speed;
    private Rigidbody2D myRigidbody;
    private Vector3 change;
    private Animator animator;
    public Text startText;
    public GameObject text;


    // Use this for initialization
    void Start () {
        currentState = PlayerState.walk;
        animator = GetComponent<Animator>();
        myRigidbody = GetComponent<Rigidbody2D>();
        StartCoroutine(showStarttext());
        animator.SetFloat("moveX", 0);
        AntiHack.RestartTimer(true);
        animator.SetFloat("moveY", -1);
    }
	
	// Update is called once per frame
	void Update () {
        change = Vector3.zero;
        change.x = Input.GetAxisRaw("Horizontal");
        change.y = Input.GetAxisRaw("Vertical");
        if (Input.GetButtonDown("attack") & currentState != PlayerState.attack)
        {
            StartCoroutine(attack_co());
        }
        else if (change != Vector3.zero & (currentState == PlayerState.walk || currentState == PlayerState.idle))
        {
            MoveCharacter();
            animator.SetFloat("moveX", change.x);
            animator.SetFloat("moveY", change.y);
            animator.SetBool("moving", true);
        } else
        {
            animator.SetBool("moving", false);
        }
	}

    private IEnumerator attack_co()
    {
        animator.SetBool("attacking", true);
        currentState = PlayerState.attack;
        yield return null;
        animator.SetBool("attacking", false);
        yield return new WaitForSeconds(.33f);
        currentState = PlayerState.walk;
    }
    void MoveCharacter()
    {
        change.Normalize();
        myRigidbody.MovePosition(transform.position + change * speed * Time.deltaTime);
    }
    public void Knock(float knockTime)
    {
        StartCoroutine(KnockCo(knockTime));
    }
    private IEnumerator showStarttext()
    {
        text.SetActive(true);
        yield return new WaitForSeconds(3f);
        text.SetActive(false);
    }
    private IEnumerator KnockCo(float knockTime)
    {
        if (myRigidbody != null)
        {
            yield return new WaitForSeconds(knockTime);
            myRigidbody.velocity = Vector2.zero;
            currentState = PlayerState.idle;
            myRigidbody.velocity = Vector2.zero;
        }
    }

}
