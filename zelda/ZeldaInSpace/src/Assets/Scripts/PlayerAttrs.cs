using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Text;
using System.IO;
using System.Security.Cryptography;
public class PlayerAttrs : MonoBehaviour {

    public GUIStyle style;
    public List<string> checkpoints;
    public string encrypted;

    void Start () {
        checkpoints = new List<string>();
        style.normal.textColor = Color.green;
        checkpoints.Add("0");
        encrypted = "";
    }


    private string Encrypt(string clearText, string key)
    {
        string EncryptionKey = key;
        byte[] clearBytes = Encoding.Unicode.GetBytes(clearText);
        using (Aes encryptor = Aes.Create())
        {
            Rfc2898DeriveBytes pdb = new Rfc2898DeriveBytes(EncryptionKey, new byte[] { 0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76 });
            encryptor.Key = pdb.GetBytes(32);
            encryptor.IV = pdb.GetBytes(16);
            using (MemoryStream ms = new MemoryStream())
            {
                using (CryptoStream cs = new CryptoStream(ms, encryptor.CreateEncryptor(), CryptoStreamMode.Write))
                {
                    cs.Write(clearBytes, 0, clearBytes.Length);
                    cs.Close();
                }
                clearText = Convert.ToBase64String(ms.ToArray());
            }
        }
        return clearText;
    }


    private string Decrypt(string cipherText, string key)
    {
        string EncryptionKey = key;
        byte[] cipherBytes = Convert.FromBase64String(cipherText);
        using (Aes encryptor = Aes.Create())
        {
            Rfc2898DeriveBytes pdb = new Rfc2898DeriveBytes(EncryptionKey, new byte[] { 0x49, 0x76, 0x61, 0x6e, 0x20, 0x4d, 0x65, 0x64, 0x76, 0x65, 0x64, 0x65, 0x76 });
            encryptor.Key = pdb.GetBytes(32);
            encryptor.IV = pdb.GetBytes(16);
            using (MemoryStream ms = new MemoryStream())
            {
                using (CryptoStream cs = new CryptoStream(ms, encryptor.CreateDecryptor(), CryptoStreamMode.Write))
                {
                    cs.Write(cipherBytes, 0, cipherBytes.Length);
                    cs.Close();
                }
                cipherText = Encoding.Unicode.GetString(ms.ToArray());
            }
        }
        return cipherText;
    }

    // Update is called once per frame
    void Update () {
		
	    }
    void OnGUI()
    {
        StringBuilder builder = new StringBuilder();
        string result;
        result = builder.ToString();
        if (checkpoints.Count >= 1) {
            foreach (string checkpoint in checkpoints)
            {
                // Append each int to the StringBuilder overload.
                builder.Append(checkpoint);
            }

            result = builder.ToString();
            if (string.Equals(checkpoints[checkpoints.Count - 1], "final"))
            {
                // try to decrypt flag
                if (string.Equals(encrypted, ""))
                {
                    try
                    {
                        encrypted = Decrypt("pI0gDg911A3Qcf++L3rvfkwIEkXsg4jq6pwOHMgG1VlpPuE9t4eljr4fQvXUa9bMJN4TL+DzQoj8aHTe1sNt+y5FND+gqn04OOltMhv/sms=", result);
                    }
                    catch (CryptographicException ex)
                    {
                        encrypted = "wrong key Zelda! :(";
                    }
                    Debug.Log(encrypted);

                }
            }
            else
            {
                encrypted = "";
            }
        }

        if (!string.Equals(result, ""))
        {
            GUI.Label(new Rect(0, 5, 400, 105), result, style);
        }
        if (!string.Equals(encrypted, ""))
        {
            GUI.Label(new Rect(0, 100, 400, 100), encrypted, style);
        }
    }
}